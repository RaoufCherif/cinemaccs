export type Day =
  | "Lundi"
  | "Mardi"
  | "Mercredi"
  | "Jeudi"
  | "Vendredi"
  | "Samedi"
  | "Dimanche";
export type Language = "VF" | "VO";
export type Session = {
  day: Day;
  date: string;
  time: string;
  language: Language;
  reservation_link: string;
};
export type Movie = {
  id: number;
  title: string;
  poster: string;
  duration: string;
  allocine_link: string;
};
export type MovieWithTheaters = Movie & {
  theaters: TheaterWithRooms[];
};
export type Room = {
  id: number;
  name: string;
  accessibility_description: string;
};
export type RoomWithTheaters = Room & {
  theater: TheaterBase;
};
export type RoomWithSessions = Room & {
  sessions: Session[];
};
export type MovieRoom = {
  movie: Movie;
  room: Room;
  sessions: Session[];
};
type TheaterBase = {
  id: number;
  name: string;
  address: string;
  accessibility_description: string;
  photos: string[];
};
export type Theater = TheaterBase & {
  movies_rooms: MovieRoom[];
};
export type TheaterWithRooms = {
  id: number;
  name: string;
  rooms: RoomWithSessions[];
};
