import { useQuery, UseQueryResult } from "@tanstack/react-query";
import { Movie, MovieWithTheaters } from "../pages/types";
import { APIQueryKey, sampleSessions } from "./utils";
import { sampleImage } from "../sample_image";

const movieWithTheaters = {
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

const movies = [
  {
    id: 2,
    title: "Les deux tours",
    poster: sampleImage,
    duration: "3H23",
    allocine_link: "https://codephenix.fr",
  },
  {
    id: 3,
    title: "Le retour du roi",
    poster: sampleImage,
    duration: "3H23",
    allocine_link: "https://codephenix.fr",
  },
  {
    id: 4,
    title: "Alabama",
    poster: sampleImage,
    duration: "3H23",
    allocine_link: "https://codephenix.fr",
  },
];

const getMovieKey = (): APIQueryKey => ["get_movie_details"];
// const fetchTheaters = async (): Promise<Theater[]> => theaters;
const fetchMovie = (): MovieWithTheaters => movieWithTheaters;
export const useGetMovie = (): UseQueryResult<MovieWithTheaters> => {
  return useQuery({ queryKey: getMovieKey(), queryFn: fetchMovie });
};

const getSearchMoviesKey = (): APIQueryKey => ["get_movie_search"];
const fetchSearchMovies = (): Movie[] => movies;
export const useGetSearchMovies = (): UseQueryResult<Movie[]> => {
  return useQuery({
    queryKey: getSearchMoviesKey(),
    queryFn: fetchSearchMovies,
  });
};
