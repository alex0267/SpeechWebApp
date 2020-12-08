import React from "react";
import ReactDOM from "react-dom";

import {Recorder} from 'react-voice-recorder';
import 'react-voice-recorder/dist/index.css';

import playIcons from '../img/play.svg';
import microphone from '../img/microphone.svg';
import pauseIcons from '../img/pause.svg';
import stopIcon from '../img/stop.svg';

const Button = ({onClick, title}) => <button onClick={onClick}>{title}</button>;

const ImageButton = ({onClick, imgPath, altText}) =>
      <div onClick={onClick}>
        <img src={imgPath} alt={altText} width="30" height="30" />
      </div>;

const Timer = ({time}) =>
      <div>
        <span>
          {time.m !== undefined
           ? `${time.m <= 9 ? "0" + time.m : time.m}`
           : "00"}
        </span>
        <span>:</span>
        <span>
          {time.s !== undefined
           ? `${time.s <= 9 ? "0" + time.s : time.s}`
           : "00"}
        </span>
      </div>;

const AudioPlayer = ({audios, show}) =>
      show ?
      <audio controls>
        <source src={audios[0]} type="audio/ogg" />
        <source src={audios[0]} type="audio/mpeg" />
      </audio>
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
            <ImageButton
              onClick={e => startRecording(e)}
              imgPath={microphone}
              altText="Microphone icon"/>
        );
    else
        return (
            <div>
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
                <div>
                  <div>
                    <Button
                      onClick={() => this.props.handleAudioUpload(this.state.audioBlob)}
                      title="Upload" />
                    <Button
                      onClick={(e) => this.handleRest(e)}
                      title="Clear" />
                  </div>
                  <AudioPlayer audios={audios} show={audioURL !== null && showUIAudio} />
                  <Timer time={time}/>
                  {!recording ? (
                      <p>Press the microphone to record</p>
                  ) : null}
                  <RecorderControls
                    recording={recording}
                    pauseRecord={pauseRecord}
                    startRecording={(e) => this.startRecording(e)}
                    stopRecording={(e) => this.stopRecording(e)}
                    handleAudioStart={(e) => this.handleAudioStart(e)}
                    handleAudioPause={(e) => this.handleAudioPause(e)}
                  />
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

