import Header from "../components/Header";
import { useEffect, useState } from "react";
import { getLevels } from "../services/api";
import type { BasicLevel } from "../types/Game";
import LevelCard from "../components/LevelCard";

const Levels: React.FC = () => {
  const [levels, setLevels] = useState<BasicLevel[]>([]);

  useEffect(() => {
    getLevels()
      .then((response) => {
        console.log(response);
        setLevels(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
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
      <section>
        {levels.map((level) => (
          <div key={level.id}>
            <LevelCard level={level} />
          </div>
        ))}
      </section>
    </div>
  );
};

export default Levels;
