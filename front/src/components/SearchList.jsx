import React from "react";
import Card from "./Card";

function SearchList({ filteredProducts }) {
  const filtered = filteredProducts.map((pdt, index) => {
    return (
      <Card
        key={index}
        pdt={pdt}
      />
    );
  });
  return (
    <div className='results'>
      <div className='listing'>{filtered}</div>
    </div>
  );
}

export default SearchList;
