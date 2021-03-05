import React from "react";
import ReactDOM from "react-dom";

const Button = ({ onClick, title, isHidden = false, extraClass = "" }) => {
  const hiddenClasses = isHidden ? " pointer-events-none bg-gray-400 " : " bg-black ";
  return (
    <button
      onClick={onClick}
      className={"button w-1/2 flex items-center justify-center rounded-full text-white px-6 py-2.5 m-2 "
        .concat(hiddenClasses)
        .concat(extraClass)}
    >
      {title}
    </button>
  );
};

const ImageButton = ({ onClick, imgPath, altText, buttonName = "" }) => (
  <div
    onClick={onClick}
    className="flex items-center justify-center p-0.5 m-0.5 cursor-pointer"
  >
    <img
      src={imgPath}
      alt={altText}
      width="30"
      height="30"
      className={buttonName}
    />
  </div>
);

export { Button, ImageButton };
