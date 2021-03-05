import React, { useState } from "react";
import ReactDOM from "react-dom";

import { Button } from "./ui.jsx";

import { apiHost, isDev } from "./constants.js";
import ReCAPTCHA from "react-google-recaptcha";

const production_client_key = "6Le_jF0aAAAAAH1_lVo_WmLd__ZNOi44YX4S1Y3L";
const captcha_site_key = isDev
  ? "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
  : production_client_key;

const Form = () => {
  const [uuid, setUuid] = useState("");
  const [error, setError] = useState("");
  const [captcha, setCaptcha] = useState("");

  function onCaptchaChange(value) {
    console.log("Captcha value:", value);
    setCaptcha(value);
  }

  const onChange = (e) => setUuid(event.target.value);
  const onSubmit = async () => {
    if (captcha == "") {
      setError("Completez le reCaptcha pour continuer.");
    } else {
      const r = await fetch(
        `${apiHost}/api/v0.1/delete_record/${uuid}?captcha_response=${captcha}`,
        {
          method: "DELETE",
        }
      );
      const json = await r.json();
      if (r.status == 200) {
        console.log(json);
        window.location = "/delete-recording-success";
      } else {
        setError(json.detail);
        setUuid("");
      }
    }
  };

  const errorMsg = error ? <p>Erreur: {error}</p> : <div></div>;

  return (
    <div className="flex flex-col items-center justify-center m-8">
      {errorMsg}
      <input
        value={uuid}
        onChange={onChange}
        placeholder="Identifiant"
        className="border-gray-400 border-2 rounded-full px-4"
      />
      <ReCAPTCHA sitekey={captcha_site_key} onChange={onCaptchaChange} />
      <Button onClick={onSubmit} title="Effacer" />
    </div>
  );
};

ReactDOM.render(<Form />, document.getElementById("form"));
