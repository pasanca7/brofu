import SearchIcon from "../utils/icons/SearchIcon";

const SearchBar: React.FC = () => {
  return (
    <form className="max-w-lg mx-auto">
      <div className="flex">
        <div className="relative w-full mb-6">
          <input
            type="text"
            placeholder="Search player..."
            className=" block p-2.5 w-full z-20 rounded-lg text-sm sm:text-xl 2xl:text-2xl text-white bg-slate-950 pl-2"
          />
          <button className="absolute top-0 end-0 p-2.5 h-full rounded-e-lg border border-slate-800 hover:bg-yellow-400 bg-yellow-600">
            <SearchIcon className="w-5 h-5 text-black" />
          </button>
        </div>
      </div>
    </form>
  );
};

export default SearchBar;
