import React, { useState } from 'react';
import Camera from 'react-html5-camera-photo';
import 'react-html5-camera-photo/build/css/index.css';
import ImagePreview from './ImagePreview';
import axios from 'axios'
import { apiUrl } from './config'

function CameraApp(props) {
   const [dataUri, setDataUri] = useState('')
   const [{ clean, confidence }, setState] = useState({ clean: null, confidence: 0 })
   function handleTakePhoto(dataUri) {
      const fd = new FormData()
      fd.append('file', dataUri)
      axios.post(apiUrl, { 'file': dataUri })
         .then((res) => {
            setState({
               clean: res.data.is_clean,
               confidence: res.data.predictedVal
            })
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
         <div><h3>The room is clean: {clean}</h3></div>
         <div><h3>PredictedVal: {confidence}</h3></div>
      </div>
   );
}
export default CameraApp