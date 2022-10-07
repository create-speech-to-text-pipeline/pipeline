// import logo from './logo.svg';
import './App.css';
import { useReactMediaRecorder } from "react-media-recorder";

function App() {
  const RecordView = () => {
    const { status, startRecording, stopRecording, mediaBlobUrl } =
      useReactMediaRecorder({ video: true });
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