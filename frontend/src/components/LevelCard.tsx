import type { BasicLevel } from "../types/Game";
import { useNavigate } from "react-router-dom";

type LevelCardProps = {
  level: BasicLevel;
};

const LevelCard: React.FC<LevelCardProps> = ({ level }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/level/${level.id}`);
  };

  return (
    <div
      onClick={handleClick}
      className="flex-col w-60 max-w-96 bg-black shadow-xl m-4 rounded-2xl p-4 border border-gray-500"
    >
      <h2 className="flex justify-center">
        {level.team} - {level.season}
      </h2>
      <img
        className="justify-center"
        src={level.logo_url}
        alt={`${level.team} logo`}
      />
    </div>
  );
};

export default LevelCard;
