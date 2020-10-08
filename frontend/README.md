# Frontend
## The frontend is divided into three components discussed below <br>
* Uploading an image to the server.
* Taking an image in real-time using the device’s camera and uploading it to the server.
* Taking an image in real-time and predict using TFJS model loaded in frontend itself.

## Blog post with more details:
Building a Reactjs front-end to interact with a Machine Learning model

![cleanvsmessy](/frontend/Demo.gif)

### Setting up the environment:
Node version-`12.18.4`
npm version-`6.14.6`
Install dependencies using:

```$ npm install```

### Run the frontend server
Build the server from current directory:
```$ npm run-script build```
Start the server using:
```$ npm start```

## Configuring the Parameters:
## Config.js:
The API URL used for prediction using a server is stored in `src/config.js`.
## Model:
The tfjs model is saved inside `public/`.
