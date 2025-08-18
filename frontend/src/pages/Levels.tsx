import Header from "../components/Header";
import { useEffect } from "react";
import api from "../services/api";

const Levels: React.FC = () => {
  useEffect(() => {
    api.get("/game/levels").then((response) => {
      console.log(response.data);
    });
  });
  return (
    <div className="h-full w-full bg-slate-800 text-white">
      <Header />
      <div className="flex justify-end p-2">
        <div className="p-1 px-2 text-black border-2 border-black border-solid rounded-md bg-yellow-600 text-sm sm:text-xl 2xl:text-2xl">
          <p>
            {"1"}/{"1000"}
          </p>
        </div>
      </div>
      <div>
        <h2>Levels</h2>
        <p>This is the Levels page.</p>
      </div>
    </div>
  );
};

export default Levels;
