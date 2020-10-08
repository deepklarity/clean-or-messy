import React, { useState } from 'react'
import Camera from 'react-html5-camera-photo'
import 'react-html5-camera-photo/build/css/index.css'
import ImagePreview from './ImagePreview'
import * as tf from '@tensorflow/tfjs'
import { imgWidth, imgHeight } from './config'

function OfflineCameraApp() {
    const [dataUri, setDataUri] = useState('')
    const [state, setState] = useState(0)
    async function handleTakePhoto(dataUri) {
        // The model is present in public folder, so that it could be downloaded over http/https
        const model = await tf.loadLayersModel('/tfjs/model.json')
        var img = new Image
        img.width = imgWidth
        img.height = imgHeight
        img.src = dataUri
        var tensorImg = tf.browser.fromPixels(img).resizeNearestNeighbor([imgWidth, imgHeight]).toFloat().expandDims()
        var prediction = model.predict(tensorImg).data()
            .then((res) => {
                setState(res)
            })
        setDataUri(dataUri)
    }
    const isFullscreen = false
    return (
        <div>
            {
                (dataUri)
                    ? <ImagePreview dataUri={dataUri}
                        isFullscreen={isFullscreen}
                    />
                    : <Camera
                        onTakePhoto={(dataUri) => { handleTakePhoto(dataUri); }}
                    />
            }
            <div><h3>The room is clean: {(state == 0 ? "" : state < 0.5 ? "True" : "False")}</h3></div>
            <div><h3>PredictedVal: {state} </h3></div>
        </div>
    );
}

export default OfflineCameraApp