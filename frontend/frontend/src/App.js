// import logo from './logo.svg';
import './App.css';
import { useReactMediaRecorder } from "react-media-recorder";

function App() {
  const record = document.querySelector(".record");
  const stop = document.querySelector(".stop");
  const soundClips = document.querySelector(".sound-clips");
  const mediaRecorder = new MediaRecorder(stream);

  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    console.log("getUserMedia supported.");
    navigator.mediaDevices
      .getUserMedia(
        // constraints - only audio needed for this app
        {
          audio: true,
        }
      )
  
      // Success callback
      .then((stream) => {})
  
      // Error callback
      .catch((err) => {
        console.error(`The following getUserMedia error occurred: ${err}`);
      });
  } else {
    console.log("getUserMedia not supported on your browser!");
  }
  record.onclick = () => {
    mediaRecorder.start();
    console.log(mediaRecorder.state);
    console.log("recorder started");
    record.style.background = "red";
    record.style.color = "black";
  };
  let chunks = [];

mediaRecorder.ondataavailable = (e) => {
  chunks.push(e.data);
};


  return (
    <div className="App">
      <p>{status}</p>
      <button onClick={startRecording}>Start Recording</button>
      <button onClick={stopRecording}>Stop Recording</button>
      <video src={mediaBlobUrl} controls autoPlay loop />
          </div>
  );
}
export default App;