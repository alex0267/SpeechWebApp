import React from "react";
import ReactDOM from "react-dom";

const Button = ({onClick, title}) =>
      <button onClick={onClick}  className="w-1/2 flex items-center justify-center rounded-md bg-black text-white p-2 m-2">
      {title}
</button>;

const ImageButton = ({onClick, imgPath, altText}) =>
      <div onClick={onClick} className="flex items-center justify-center p-0.5 m-0.5 cursor-pointer">
      <img src={imgPath} alt={altText} width="30" height="30" />
      </div>;

export {
    Button,
    ImageButton
}
