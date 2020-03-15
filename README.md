# DrowsyDriver

DrowsyDriver is a application that identifies if the driver is drowsy give a alert .

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## CRUX
Detects face from the frame, then detects eyes from the face region, sometimes the haarcascade may misbehave and detect other parts so only upper region of face is taken for eyes.Left eye and Right eye are identified based on the location of bounding box in the face region.Then Region of interest is cut out(Each eyes are taken) and for each eye eyebrows are removed after that , the eadges of eyes are detected with cannyedges and noices are removed . Now we got the eye region so we note for shinking of eye region , then alerts the driver

## Skills Used
###  Library 
![OpenCv](https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/OpenCV_Logo_with_text.png/195px-OpenCV_Logo_with_text.png)
### Language
![python](https://camo.githubusercontent.com/319c77f52d0ef90ae90152ee32d7f25042cb954d/687474703a2f2f7777772e706e67616c6c2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031362f30352f507974686f6e2d4c6f676f2d467265652d446f776e6c6f61642d504e472e706e67)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

