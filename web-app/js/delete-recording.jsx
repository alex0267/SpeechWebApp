import React, { useState } from "react";
import ReactDOM from "react-dom";


const Form = () => {
    const [uuid, setUuid] = useState("");
    const [error, setError] = useState("");

    const onChange = e => setUuid(event.target.value);
    const onSubmit = async () => {
        const r = await fetch(`/api/v0.1/delete_record/${uuid}`, {
            method: "DELETE",
        });
        const json = await r.json();
        if (r.status == 200) {
            console.log(json);
            window.location = "/delete-recording-success.html";
        } else {
            setError(json.detail);
            setUuid("");
        }
    };

    const errorMsg = error ? <p>Error: {error}</p> : <div></div>;

    return (
        <div>
          { errorMsg }
          <input
            value={uuid}
            onChange={onChange}
            placeholder="Recording UUID"
            className="border-gray-400 border-2 rounded-full px-4" />
          <div onClick={onSubmit}>Submit</div>
        </div>
    );
};

ReactDOM.render(
    <Form />,
    document.getElementById("form")
);
