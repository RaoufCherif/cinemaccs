export type Day =
  | "Lundi"
  | "Mardi"
  | "Mercredi"
  | "Jeudi"
  | "Vendredi"
  | "Samedi"
  | "Dimanche";
export type AccessPoint = "bottom" | "middle" | "top";
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
  access_point?: AccessPoint;
  photos?: string[];
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

export type TheaterBase = {
  id: number;
  name: string;
  address: string;
  accessibility_description: string;
  sanitory_description: string;
  popcorn_description: string;
  entry_description: string;
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
