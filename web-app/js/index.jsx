import React from "react";
import ReactDOM from "react-dom";

import {Recorder} from 'react-voice-recorder';
import 'react-voice-recorder/dist/index.css';

import playIcons from '../img/play.svg';
import microphone from '../img/microphone.svg';
import pauseIcons from '../img/pause.svg';
import stopIcon from '../img/stop.svg';

const Button = ({onClick, title}) =>
      <button onClick={onClick}  className="w-1/2 flex items-center justify-center rounded-md bg-black text-white p-2 m-2">
        {title}
      </button>;

const ImageButton = ({onClick, imgPath, altText}) =>
      <div onClick={onClick} className="flex items-center justify-center p-0.5 m-0.5">
        <img src={imgPath} alt={altText} width="30" height="30" />
      </div>;

const Timer = ({time, show}) => {
    if (!show)
        return <div />;
    else
        return (
            <div className="flex justify-center items-center w-80 h-12 p-2 m-2 bg-gray-400 rounded-full">
              {time.m !== undefined
               ? `${time.m <= 9 ? "0" + time.m : time.m}`
               : "00"}
              :
              {time.s !== undefined
               ? `${time.s <= 9 ? "0" + time.s : time.s}`
               : "00"}
            </div>
        );
};

const AudioPlayer = ({audios, show}) =>
      show ?
      <div  className="flex items-center justify-center p-2 m-2 h-12">
        <audio controls className="w-80 rounded-full">
            <source src={audios[0]} type="audio/ogg" />
            <source src={audios[0]} type="audio/mpeg" />
        </audio>
      </div>
      :
      <div />;

const RecorderControls = props => {
    const {
        recording,
        pauseRecord,
        startRecording,
        stopRecording,
        handleAudioStart,
        handleAudioPause,
    } = props;
    if (!recording)
        return (
            <div className="flex items-center justify-center w-20">
                <ImageButton
                onClick={e => startRecording(e)}
                imgPath={microphone}
                altText="Microphone icon"/>
            </div>
        );
    else
        return (
            <div className="flex items-center justify-center w-20">
              <ImageButton
                onClick={e => stopRecording(e)}
                imgPath={stopIcon}
                altText="Stop icon"/>
              <ImageButton
                onClick={e => !pauseRecord ? handleAudioPause(e) : handleAudioStart(e)}
                imgPath={pauseRecord ? playIcons : pauseIcons}
                altText={pauseRecord ? "Play icon" : "Pause icon"} />
            </div>
        );
}

class MyRecorder extends Recorder {
    render() {
        const { recording, audios, time, medianotFound, pauseRecord } = this.state;
        const { showUIAudio, title, audioURL } = this.props;

        if (medianotFound)
            return  (
                <p style={{ color: "#fff", marginTop: 30, fontSize: 25 }}>
                  Seems the site is Non-SSL
                </p>
            );
        else
            return (
                <div className="flex flex-row">
                  <RecorderControls
                    recording={recording}
                    pauseRecord={pauseRecord}
                    startRecording={(e) => this.startRecording(e)}
                    stopRecording={(e) => this.stopRecording(e)}
                    handleAudioStart={(e) => this.handleAudioStart(e)}
                    handleAudioPause={(e) => this.handleAudioPause(e)}
                  />
                  <Timer time={time} show={audioURL === null}/>
                  <AudioPlayer audios={audios} show={audioURL !== null && showUIAudio} />
                  <div className="flex flex-row">
                    <Button
                      onClick={() => this.props.handleAudioUpload(this.state.audioBlob)}
                      title="Upload" />
                    <Button
                      onClick={(e) => this.handleRest(e)}
                      title="Clear" />
                  </div>
                </div>
            );
    }
}

class VoiceRecorder extends React.Component {
    constructor() {
        super();
        this.state = {
            audioDetails: {
                url: null,
                blob: null,
                chunks: null,
                duration: {
                    h: 0,
                    m: 0,
                    s: 0
                }
            }
        };
    }
    handleAudioStop(data){
        console.log(data);
        this.setState({ audioDetails: data });
    }
    handleAudioUpload(file) {
        console.log(file);
    }
    handleRest() {
        const reset = {
            url: null,
            blob: null,
            chunks: null,
            duration: {
                h: 0,
                m: 0,
                s: 0
            }
        };
        this.setState({ audioDetails: reset });
    }
    render() {
        return (
            <MyRecorder
                record={true}
                title={"New recording"}
                audioURL={this.state.audioDetails.url}
                showUIAudio
                handleAudioStop={data => this.handleAudioStop(data)}
                handleAudioUpload={data => this.handleAudioUpload(data)}
                handleRest={() => this.handleRest()}
            />
        );
    }
}


ReactDOM.render(<VoiceRecorder />, document.getElementById("root"));

