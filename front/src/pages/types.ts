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
  id: string;
  title: string;
  poster: string;
  duration: string;
  allocine_link: string;
};
export type Room = {
  id: string;
  name: string;
};
export type MovieRoom = {
  movie: Movie;
  room: Room;
  sessions: Session[];
};
export type Theater = {
  id: string;
  name: string;
  address: string;
  accessibility_description: string;
  photos: string[];
  movies_rooms: MovieRoom[];
};
