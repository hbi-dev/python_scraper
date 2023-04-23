import React from "react";

function Card({ pdt, key }) {
  const getCurency = (price) => {
    if (Number.isInteger(price)) {
      return price + " €";
    }
    if (price.includes("$")) {
      return price.substring(1) + " $";
    }
    if (price.includes("€")) {
      return price.slice(0, -1) + "€";
    }
  };

  return (
    <>
      <div
        className='card'
        key={key}
      >
        <div className='site'>{pdt.site}</div>
        <div className='model'>
          <a
            href={pdt.url}
            // eslint-disable-next-line
            target="_blank" rel="noreferrer"
          >
            {pdt.brand}
          </a>
        </div>
        <div className='price'>{getCurency(pdt.price)}</div>
      </div>
    </>
  );
}

export default Card;
