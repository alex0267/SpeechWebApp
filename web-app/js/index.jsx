import React from "react";
import ReactDOM from "react-dom";

import {Recorder} from 'react-voice-recorder';
import 'react-voice-recorder/dist/index.css';

import { Button, ImageButton } from "./ui.jsx";

import playIcons from '../img/play.svg';
import microphone from '../img/microphone.svg';
import pauseIcons from '../img/pause.svg';
import stopIcon from '../img/stop.svg';

import { apiHost } from './constants.js';


import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';


const Timer = ({time, show}) => {
    if (!show)
        return <div />;
    else
        return (
            <div className="flex justify-center items-center w-11/12 h-12 p-2 m-2 bg-gray-400 rounded-full">
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
      <div  className="flex items-center justify-center m-2 h-12 w-full">
        <audio controls className="w-11/12 rounded-full">
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
                altText="Microphone icon"
                buttonName="microphone-button"/>
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

        if (this.props.uuid)
            return (
                <p>
                  Vous pouvez <a href="/delete-recording.html">supprimer</a> cet enregistrement avec cet identifiant: {this.props.uuid}
                </p>
            );

        if (medianotFound)
            return  (
                <p style={{ color: "#fff", marginTop: 30, fontSize: 25 }}>
                  Seems the site is Non-SSL
                </p>
            );
        else
            return (
                <div className="flex flex-col justify-center items-center w-11/12">
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
                      title="Sauvegarder" />
                    <Button
                      onClick={(e) => this.handleRest(e)}
                      title="Effacer" />
                  </div>
                </div>
            );
    }
}

class VoiceRecorder extends React.Component {
    constructor(props) {
        super(props);
        const state = {
            sentence_info: {
                sentence: '',
                id: -1,
            },
        };
        for (let emotion of this.props.emotions) {
            state[emotion] = {
                url: null,
                blob: null,
                chunks: null,
                duration: {
                    h: 0,
                    m: 0,
                    s: 0
                },
                iiud: null,
            };
        }
        this.state = state;
        this.updateSentence();
    }
    resetRecords() {
        for (let emotion of this.props.emotions) {
            this.setState({
                ...this.state,
                [emotion]: {
                    url: null,
                    blob: null,
                    chunks: null,
                    duration: {
                        h: 0,
                        m: 0,
                        s: 0
                    },
                    iiud: null,
                }
            });
        }
    }
    async updateSentence() {
        const resp = await fetch(`${apiHost}/api/v0.1/get_random_sentence/`);
        const sentence_info = await resp.json();
        this.setState({ ...this.state, sentence_info });
        this.resetRecords();
    }
    handleAudioStop(emotion) {
        return data => this.setState({ ...this.state, [emotion]: data });
    }
    updateUuid(emotion, uuid) {
        const newData = {
            ...this.state[emotion],
            uuid,
        };
        this.setState({ ...this.state, [emotion]: newData });
    }
    handleAudioUpload(emotion) {
        return file => {
            const data = new FormData();
            data.append('file', file);
            const url = `${apiHost}/api/v0.1/create_record/${emotion}?sentence_id=${this.state.sentence_info.id}`;

            fetch(url, {
                method: 'POST',
                body: data
            })
                .then(r => r.json())
                .then(data => this.updateUuid(emotion, data.uuid));
        };
    }
    handleRest(emotion) {
        return () => {
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
            this.setState({ ...this.state, [emotion]: reset });
        };
    }
    render() {
        const emotion = this.props.emotions[0];
        const emotiontab =this.props.emotions.map((emotion, i) =>
            <Tab key={i}>
                {emotion}
            </Tab>
        );
        const recorders = this.props.emotions.map((emotion, i) =>
            <TabPanel key={i}>
                <MyRecorder
                    record={true}
                    title={emotion}
                    audioURL={this.state[emotion].url}
                    showUIAudio
                    handleAudioStop={data => this.handleAudioStop(emotion)(data)}
                    handleAudioUpload={data => this.handleAudioUpload(emotion)(data)}
                    handleRest={() => this.handleRest(emotion)()}
                    uuid={this.state[emotion].uuid}
                />
            </TabPanel>                  
        );

        return (
            <div>
              <div className="flex flex-col items-center">
                <p className="p-2 mx-2 mt-8">Phrase à prononcer selon l'émotion sélectionnée: </p>
                <h3 className="p-2 mx-2 mt-2">
                  <span>
                      {this.state.sentence_info.sentence}
                  </span>
                </h3>
                <Button onClick={() => this.updateSentence()} title='Autre phrase' extraClass="w-3/12 mb-8" />
              </div>
              <Tabs>
                <div className="tab-wrapper">
                <TabList>
                    {emotiontab}
                </TabList>
                </div>
                <div className="scroll-arrows">
                  <div className="float-left">&lt;</div>
                  <div className="float-right">&gt;</div>
                </div>
                {recorders}
              </Tabs>

              
            </div>
        );
    }
}


const sentence = "Il faut avoir voulu mourir, Maximilien, pour savoir combien il est bon de vivre.";
const emotions = ['Joie', 'Tristesse', 'Colère', 'Dégoût', 'Peur', 'Neutre'];
ReactDOM.render(
    <VoiceRecorder emotions={emotions} sentence={sentence} />,
    document.getElementById("root")
);
