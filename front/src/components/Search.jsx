import React, { useState } from "react";
import Scroll from "./Scroll";
import SearchList from "./SearchList";

function Search({ details }) {
  const [searchField, setSearchField] = useState("");

  const filteredProducts = details.filter((produit) => {
    return (
      produit.brand.toLowerCase().includes(searchField.toLowerCase()) ||
      produit.price.toString().match(searchField) != null
    );
  });
  const handleChange = (e) => {
    setSearchField(e.target.value);
  };

  //const filtersList = [...new Set(details.map((item) => item.site))];

  function searchList() {
    return (
      <Scroll>
        <SearchList filteredProducts={filteredProducts} />
      </Scroll>
    );
  }

  return (
    <>
      <div className='container'>
        <div className='search'>
          <input
            className='searchBar'
            type='search'
            placeholder='filtre par modele ou prix '
            onChange={handleChange}
          />
        </div>
        <h3 className='results_h3'>
          nombres de resultats : {filteredProducts.length}{" "}
        </h3>
        {/* <div className='filters'>
          {filtersList.map((item, index) => {
            return <button key={index}>{item}</button>;
          })}
        </div> */}
        <div className='underline'></div>
        <div>{searchList()}</div>
      </div>
    </>
  );
}

export default Search;
