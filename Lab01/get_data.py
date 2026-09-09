import urllib.request, zipfile, os

def download_data(force=False):
    """Download and extract course data from Zenodo."""
    
    zip_path = 'data.zip'
    data_dir = './data'
    
    if not os.path.exists(zip_path) or force:
        print("Downloading course data...")
        urllib.request.urlretrieve(
            'https://zenodo.org/records/18235955/files/data.zip?download=1',
            zip_path
        )
        print("Download complete")
    
    if not os.path.exists(data_dir) or force:
        print("Extracting data files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        print("Data extracted")
    
    return data_dir

<<<<<<< HEAD:get_data.py
download_data()


#This is awesome 
=======

if __name__ == "__main__":
    download_data()

>>>>>>> 86d7a7e052c1ceee863492ae8001b6dddddb4e35:Lab01/get_data.py
