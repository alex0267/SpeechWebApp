import React from "react";
import ReactDOM from "react-dom";

import {Recorder} from 'react-voice-recorder';
import 'react-voice-recorder/dist/index.css';

import playIcons from '../img/play.svg';
import microphone from '../img/microphone.svg';
import pauseIcons from '../img/pause.svg';
import stopIcon from '../img/stop.svg';

class MyRecorder extends Recorder {
    render() {
        const { recording, audios, time, medianotFound, pauseRecord } = this.state;
        const { showUIAudio, title, audioURL } = this.props;
        const closeIcons = "";
        return (
            <div>
              {!medianotFound ? (
                  <div>
                    <div>
                      <button
                        onClick={() =>
                            this.props.handleAudioUpload(this.state.audioBlob)
                        }
                      >
                        Upload
                      </button>
                      <button onClick={(e) => this.handleRest(e)}>
                        Clear
                      </button>
                    </div>
                    <div>
                      <div>
                        {audioURL !== null && showUIAudio ? (
                            <audio controls>
                              <source src={audios[0]} type="audio/ogg" />
                              <source src={audios[0]} type="audio/mpeg" />
                            </audio>
                        ) : null}
                      </div>
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
                      </div>
                      {!recording ? (
                          <p>Press the microphone to record</p>
                      ) : null}
                    </div>
                    {!recording ? (
                        <a
                          onClick={e => this.startRecording(e)}
                          href=" #"
                        >
                          <img src={microphone} width={30} height={30} alt="Microphone icons" />
                        </a>
                    ) : (
                        <div>
                          <a
                            onClick={e => this.stopRecording(e)}
                            href=" #"
                          >
                            <img src={stopIcon} width={20} height={20} alt="Stop icons" />
                          </a>
                          <a
                            onClick={
                                !pauseRecord
                                    ? e => this.handleAudioPause(e)
                                    : e => this.handleAudioStart(e)
                            }
                            href=" #"
                          >
                            {pauseRecord ? <img src={playIcons} width={20} height={20} alt="Play icons" /> : <img src={pauseIcons} width={20} height={20} alt="Pause icons" />}
                          </a>
                        </div>
                    )}
                  </div>
              ) : (
                  <p style={{ color: "#fff", marginTop: 30, fontSize: 25 }}>
                    Seems the site is Non-SSL
                  </p>
              )}
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

