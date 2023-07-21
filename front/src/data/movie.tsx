import { useQuery, UseQueryResult } from "@tanstack/react-query";
import { Movie } from "../pages/types";
import { APIQueryKey } from "./utils";

const movie = {
  id: "2",
  title: "Les deux tours",
  poster: "XXXX",
  duration: "3H23",
  allocine_link: "https://codephenix.fr",
} as Movie;

const getMovieKey = (): APIQueryKey => ["get_movie_detail"];
// const fetchTheaters = async (): Promise<Theater[]> => theaters;
const fetchMovie = (): Movie => movie;
export const useGetTheaters = (): UseQueryResult<Movie> => {
  return useQuery({ queryKey: getMovieKey(), queryFn: fetchMovie });
};
