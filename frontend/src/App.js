import React, { Component } from 'react'
import CameraApp from './Camera'
import OfflineCameraApp from './OfflineCamera'
import './App.css'
import axios from 'axios'
import { apiUrl } from './config'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      selectedFile: null,
      cleanOrMessy: "",
      predictedVal: "",
    }
  }

  fileSelectedHandler = event => {
    this.setState({
      selectedFile: event.target.files[0]
    })
  }

  fileUploadHandler = () => {
    var fd = new FormData()
    fd.append('file', this.state.selectedFile)
    axios.post(apiUrl, fd)
      .then(res => {
        this.setState({
          isLoaded: true,
          cleanOrMessy: res.data["is_clean"],
          predictedVal: res.data["predictedVal"]
        });
        return res
      });
  }

  offlineCameraAppHandler = () => {
    var x = document.getElementById("camera1")
    var y = document.getElementById("camera")
    x.classList.toggle("App-camera")
    y.classList.add("App-camera")
  }

  openCameraHandler = () => {
    var x = document.getElementById("camera")
    var y = document.getElementById("camera1")
    x.classList.toggle("App-camera")
    y.classList.add("App-camera")
  }

  render() {
    return (
      <div className="App">
        <input type="file" onChange={this.fileSelectedHandler} />
        <button onClick={this.fileUploadHandler}>Upload</button>
        <button onClick={this.openCameraHandler}>take a photo</button>
        <button onClick={this.offlineCameraAppHandler}>offline prediction</button>
        <div><h3>The room is clean: {this.state.cleanOrMessy}</h3></div>
        <div><h3>PredictedVal: {this.state.predictedVal}</h3></div>
        <div id="camera" className="App-camera">
          <CameraApp />
        </div>
        <div id="camera1" className="App-camera">
          <OfflineCameraApp />
        </div>
      </div>
    );
  }
}
export default App;
