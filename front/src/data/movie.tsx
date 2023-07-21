import { useQuery, UseQueryResult } from "@tanstack/react-query";
import { Movie, MovieWithTheaters } from "../pages/types";
import { APIQueryKey, sampleSessions } from "./utils";
import { sampleImage } from "../sample_image";

const movie = {
  id: 2,
  title: "Les deux tours",
  poster: sampleImage,
  duration: "3H23",
  allocine_link: "https://codephenix.fr",
  theaters: [
    {
      id: 1,
      name: "Bibliothèque",
      rooms: [{ id: 1, name: "Salle2", sessions: sampleSessions }],
    },
  ],
} as MovieWithTheaters;

const getMovieKey = (): APIQueryKey => ["get_movie_details"];
// const fetchTheaters = async (): Promise<Theater[]> => theaters;
const fetchMovie = (): MovieWithTheaters => movie;
export const useGetMovie = (): UseQueryResult<MovieWithTheaters> => {
  return useQuery({ queryKey: getMovieKey(), queryFn: fetchMovie });
};
