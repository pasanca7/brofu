import { useState } from "react";
import { players as mockPlayers } from "./mocks/players.json";
import { level as mockLevel } from "./mocks/level.json";
import Header from "./components/Header";
import TeamSeason from "./components/TeamSeason";
import SearchBar from "./components/searchBar";
import Table from "./components/Table";

function App() {
  const [level, setLevel] = useState(mockLevel);
  const [players, setPlayers] = useState(mockPlayers);
  const [correctPlayersId, setCorrectPlayersId] = useState<number[]>([
    1, 5, 6, 8, 10, 17, 20, 22, 28, 31, 33,
  ]);

  return (
    <div className="h-full w-full bg-slate-800 text-white">
      <Header />
      <div className="w-full overflow-y-auto p-5">
        <div className="flex items-center">
          <TeamSeason
            imageUrl={level.imageUrl}
            alt={level.team + " logo"}
            title={level.team + " " + level.season}
          />
          <div>
            <div className="flex-1 p-1 px-2 text-black border-2 border-black border-solid rounded-md bg-yellow-600 text-sm sm:text-xl 2xl:text-2xl">
              <p>
                {correctPlayersId.length}/{players.length}
              </p>
            </div>
          </div>
        </div>
      </div>
      <div className="flex flex-col p-5 pt-0">
        <SearchBar />

        <Table
          columns={["Country", "Name", "Position"]}
          rows={players}
          correctPlayersId={correctPlayersId}
        />
      </div>
    </div>
  );
}

export default App;
