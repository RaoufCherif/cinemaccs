import { useQuery, UseQueryResult } from "@tanstack/react-query";
import { MovieWithTheaters, Room, RoomWithTheaters } from "../pages/types";
import { APIQueryKey } from "./utils";

const room = {
  id: 2,
  name: "Salle 2",
  accessibility_description: "une description",
  theater: { id: 1, name: "MK2 Biblio" },
} as RoomWithTheaters;

const getRoomKey = (): APIQueryKey => ["get_room_details"];
// const fetchTheaters = async (): Promise<Theater[]> => theaters;
const fetchRoom = (): RoomWithTheaters => room;
export const useGetRoom = (): UseQueryResult<RoomWithTheaters> => {
  return useQuery({ queryKey: getRoomKey(), queryFn: fetchRoom });
};
