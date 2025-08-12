import type React from "react";

type TeamSeasonProps = {
  imageUrl: string;
  alt: string;
  title: string;
};

const TeamSeason: React.FC<TeamSeasonProps> = ({ imageUrl, alt, title }) => {
  return (
    <div className="flex-8 flex gap-2 items-center">
      <img
        className="size-10 sm:size-15 2xl:size-20"
        src={imageUrl}
        alt={alt}
      />
      <h1 className="font-bold justify-center text-sm sm:text-xl 2xl:text-2xl">
        {title}
      </h1>
    </div>
  );
};

export default TeamSeason;
