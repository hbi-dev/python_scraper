import React, { useState, useEffect } from "react";
import Search from "./components/Search";

function App() {
  const [allItems, setItems] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const nike = await fetch("http://127.0.0.1:8080/nike");
      const nike_data = await nike.json();
      const size = await fetch("http://127.0.0.1:8080/size");
      const size_data = await size.json();
      const farfetch = await fetch("http://127.0.0.1:8080/farfetch");
      const farfetch_data = await farfetch.json();
      const data = [...nike_data, ...size_data, ...farfetch_data];
      setItems(data);
    }
    fetchData();
  }, []);

  return (
    <>
      <Search details={allItems} />
    </>
  );
}

export default App;
