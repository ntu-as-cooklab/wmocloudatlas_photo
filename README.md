# WMO Cloud Atlas Photo
Python Script to Download Labeled Cloud Photo from "www.wmocloudatlas.org"

## What's this?
The cloud photos are labeled and can use to train in machine learning or other purpose.

## How to get photo
Click green button `Clone or download`, and choose `Download ZIP`. Unzip and I saved all photo in the `photo` folder.

## Run Sript 
I write in Python 2.7

You don't have to run the code, beacause there are photos already in the folder `photo`.

But if you like, you can try :)

```
git clone https://github.com/tigercosmos/wmocloudatlas_photo.git
cd wmocloudatlas_photo
# Get the link from raw HTML, but I have done it
python makePageLink.py
# Get the photo link and download
python getPhoto.py
```