import React from "react";

const Header: React.FC = () => {
  return (
    <header
      className="top-0 left-0 w-full z-10 p-2 pl-5 
    bg-gradient-to-br from-slate-950 via-slate-900 to-yellow-500
    text-white text-2xl font-bold border-b-2 border-black"
    >
      <h1>Brofu</h1>
    </header>
  );
};

export default Header;
