from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Paddy Rice Imagery"
PROJECT_NAME_FULL: str = "Paddy Rice Imagery Dataset for Panicle Segmentation"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Agricultural()]
CATEGORY: Category = Category.Agriculture(extra=Category.Drones())

CV_TASKS: List[CVTask] = [CVTask.InstanceSegmentation(), CVTask.SemanticSegmentation(), CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2021-01-10"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://zenodo.org/record/4444741#.YlAuZX9Bzmg"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 6764694
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/paddy-rice-panicle-detection"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "128.zip": "https://zenodo.org/record/4444741/files/128.zip?download=1",
    "256.zip": "https://zenodo.org/record/4444741/files/256.zip?download=1",
    "512.zip": "https://zenodo.org/record/4444741/files/512.zip?download=1",
    "basic dataset.zip": "https://zenodo.org/record/4444741/files/basic%20dataset.zip?download=1",
    "label_map.txt": "https://zenodo.org/record/4444741/files/label_map.txt?download=1",
    "README.txt": "https://zenodo.org/record/4444741/files/README.txt?download=1",
    "refined dataset.zip": "https://zenodo.org/record/4444741/files/refined%20dataset.zip?download=1",
    "splitting.ipynb": "https://zenodo.org/record/4444741/files/splitting.ipynb?download=1",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = "https://www.mdpi.com/2073-4395/11/8/1542#sec4-agronomy-11-01542"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = "https://zenodo.org/record/4444741/export/hx"
AUTHORS: Optional[List[str]] = ["Hao Wang", "Suxing Lyu", "Yaxin Ren"]
AUTHORS_CONTACTS: Optional[List[str]] = ["wangh@nercita.org.cn", "johnlyu@bpe.agr.hokudai.ac.jp", "renyx@nercita.org.cn"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = ["Beijing Academy of Agriculture and Forestry Sciences, China", "Hokkaido University, Japan"]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = ["https://goodberry-eu.eu/team/consortium/baafs/", "https://www.global.hokudai.ac.jp/"]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = None
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
