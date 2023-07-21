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
};
export type Theater = TheaterBase & {
  address: string;
  accessibility_description: string;
  photos: string[];
  movies_rooms: MovieRoom[];
};
export type TheaterWithRooms = TheaterBase & {
  rooms: RoomWithSessions[];
};
