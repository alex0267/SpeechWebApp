import React, { useState } from "react";
import ReactDOM from "react-dom";

import { Button } from "./ui.jsx";

import { apiHost } from './constants.js';

const Form = () => {
    const [uuid, setUuid] = useState("");
    const [error, setError] = useState("");

    const onChange = e => setUuid(event.target.value);
    const onSubmit = async () => {
        const r = await fetch(`${apiHost}/api/v0.1/delete_record/${uuid}`, {
            method: "DELETE",
        });
        const json = await r.json();
        if (r.status == 200) {
            console.log(json);
            window.location = "/delete-recording-success";
        } else {
            setError(json.detail);
            setUuid("");
        }
    };

    const errorMsg = error ? <p>Erreur: {error}</p> : <div></div>;

    return (
        <div className="flex flex-col items-center justify-center m-8">
          { errorMsg }
          <input
            value={uuid}
            onChange={onChange}
            placeholder="Identifiant"
            className="border-gray-400 border-2 rounded-full px-4" />
          <Button onClick={onSubmit} title="Effacer" />
        </div>
    );
};

ReactDOM.render(
    <Form />,
    document.getElementById("form")
);
