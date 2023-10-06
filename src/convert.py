# https://zenodo.org/record/4444741#.YlAuZX9Bzmg

import base64
import io
import os
from collections import defaultdict

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from PIL import Image
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    mkdir,
    remove_dir,
)
from supervisely.io.json import load_json_file


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:

    # project_name = "Rice Panicle"
    dataset_path = "/home/grokhi/rawdata/paddy-rice-panicle-detection/RE-JSON"
    batch_size = 3
    images_ext = ".png"


    def create_ann(image_path):
        labels = []

        img_height = name_to_shape[get_file_name(image_path)][0]
        img_wight = name_to_shape[get_file_name(image_path)][1]

        poly_data = name_to_polygons[get_file_name(image_path)]
        for polygons_coords in poly_data:
            exterior = []
            for coords in polygons_coords:
                exterior.append(list(reversed(coords)))

            polygon = sly.Polygon(exterior)
            label_poly = sly.Label(polygon, obj_class)
            labels.append(label_poly)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


    obj_class = sly.ObjClass("panicle", sly.Polygon)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class])
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in os.listdir(dataset_path):
        if ds_name == "temp":
            continue
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        jsons_path = os.path.join(dataset_path, ds_name)
        jsons_names = os.listdir(jsons_path)

        name_to_shape = {}
        name_to_polygons = defaultdict(list)

        temp_img_names = []
        temp_folder = os.path.join(dataset_path, "temp")
        mkdir(temp_folder)
        for curr_json_name in jsons_names:
            curr_image_name = get_file_name(curr_json_name) + images_ext
            temp_img_names.append(curr_image_name)
            curr_json_path = os.path.join(jsons_path, curr_json_name)
            data_json = load_json_file(curr_json_path)
            polygons = data_json["shapes"]

            base64_str = data_json["imageData"]
            img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
            name_to_shape[get_file_name(curr_json_name)] = (img.height, img.width)

            for curr_poly in polygons:
                name_to_polygons[get_file_name(curr_json_name)].append(curr_poly["points"])

            curr_image_path = os.path.join(temp_folder, curr_image_name)
            img.save(curr_image_path)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(jsons_names))

        for img_names_batch in sly.batched(temp_img_names, batch_size=batch_size):
            images_pathes_batch = [
                os.path.join(temp_folder, image_name) for image_name in img_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
            api.annotation.upload_anns(img_ids, anns_batch)

            progress.iters_done_report(len(img_names_batch))
        remove_dir(temp_folder)
    return project


