import React from "react";
import ReactDOM from "react-dom";

const Button = ({onClick, title, extraClass=''}) =>
      <button onClick={onClick} className={"button w-1/2 flex items-center justify-center rounded-full bg-black text-white px-6 py-2.5 m-2 ".concat(extraClass)}>
      {title}
</button>;

const ImageButton = ({onClick, imgPath, altText, buttonName=''}) =>
      <div onClick={onClick} className="flex items-center justify-center p-0.5 m-0.5 cursor-pointer">
            <img src={imgPath} alt={altText} width="30" height="30" className={buttonName} />
      </div>;

export {
    Button,
    ImageButton
}
