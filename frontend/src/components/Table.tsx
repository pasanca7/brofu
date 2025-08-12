import type React from "react";
import type { Player } from "../types/Player";
import { getFlagEmoji } from "../utils/Flags";

type TableProps = {
  rows: Player[];
  columns: string[];
  correctPlayersId: number[];
};

const Table: React.FC<TableProps> = ({ rows, columns, correctPlayersId }) => {
  return (
    <table className="border-2 border-black border-solid rounded-md text-sm sm:text-xl 2xl:text-2xl">
      <thead>
        <tr>
          {columns.map((column) => {
            return (
              <th
                key={column}
                className="border-2 border-black border-solid rounded-md bg-yellow-600 text-black text-sm sm:text-xl 2xl:text-2xl"
              >
                {column}
              </th>
            );
          })}
        </tr>
      </thead>
      <tbody>
        {rows.map((row) => {
          return (
            <tr
              className={
                correctPlayersId.includes(row.id) ? "bg-green-800" : ""
              }
              key={row.id}
            >
              <td className="text-center border-2 border-black border-solid rounded-md text-sm sm:text-xl 2xl:text-2xl">
                {getFlagEmoji(row.country)}
              </td>
              <td className="text-center border-2 border-black border-solid rounded-md text-sm sm:text-xl 2xl:text-2xl">
                {correctPlayersId.includes(row.id) ? row.name : "-"}
              </td>
              <td className="text-center border-2 border-black border-solid rounded-md text-sm sm:text-xl 2xl:text-2xl">
                {row.position}
              </td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

export default Table;
