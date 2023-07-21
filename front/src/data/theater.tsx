import { useQuery, UseQueryResult } from "@tanstack/react-query";
import { Theater } from "../pages/types";
import { APIQueryKey } from "./utils";
import { sampleImage } from "../sample_image";

const theaters = [
  {
    id: "1",
    name: "MK2 Bibliothèque",
    address: "2 rue de la bibliothèque, 75014 Paris",
  },
  {
    id: "2",
    name: "MK2 Bastille",
    address: "2 rue de la Bastille, 75014 Paris",
  },
  {
    id: "3",
    name: "MK2 Beaubourg",
    address: "2 rue de Beaubourg, 75014 Paris",
  },
] as Theater[];

const getTheatersKey = (): APIQueryKey => ["get_theaters"];
// const fetchTheaters = async (): Promise<Theater[]> => theaters;
const fetchTheaters = (): Theater[] => theaters;
export const useGetTheaters = (): UseQueryResult<Theater[]> => {
  return useQuery({ queryKey: getTheatersKey(), queryFn: fetchTheaters });
};

// export const useGetTheaters = (): UseQueryResult<Theater[]> => {
//     return useQuery(getTheatersKey(), useAPIQuery<Theater[]>("/theaters/"));
// };
// export const useAPIQuery = <RT = JSONValue,>(
//   urlPart: string,
//   searchParams?: RequestSearchParams,
//   headers: Record<string, string> = {},
//   method: HttpVerb = "GET"
// ): APIQueryFN<RT> => {
//   const dispatch = useDispatch();
//   const currentVersion = useSelector(apiVersionSelector);
//   const apiVersionMismatch = useSelector(apiVersionMismatchSelector);
//   const impersonate = useSelector(impersonatingSelector);
//   if (impersonate) {
//     headers.impersonate = impersonate.toString();
//   }

//   return (context) => {
//     const [queryKey, requestParams] = context.queryKey || [];
//     const { urlValues, searchParams: searchParams_ } = requestParams || {};

//     const handler403 = (err: AjaxError): void =>
//       handle403(dispatch, err, urlPart, queryKey, !!impersonate);

//     const resp: CancelablePromise<RT> = baseRequest(
//       method,
//       formatUrl(urlPart, urlValues, { ...searchParams, ...searchParams_ }),
//       dispatch,
//       currentVersion,
//       apiVersionMismatch,
//       queryKey,
//       undefined,
//       headers,
//       handler403
//     );
//     return resp;
//   };
// };

const movie_room = {
  movie: {
    id: "1",
    title: "Le chat poté",
    poster: sampleImage,
    duration: "3H12",
    allocine_link: "https://codephenix.fr",
  },
  room: {
    id: "1",
    name: "Salle 1",
  },
  sessions: [
    {
      day: "Vendredi",
      date: "2021-10-10",
      time: "20:00",
      language: "VF",
      reservation_link: "https://codephenix.fr",
    },
    {
      day: "Vendredi",
      date: "2021-10-10",
      time: "22:00",
      language: "VO",
      reservation_link: "https://codephenix.fr",
    },
    {
      day: "Samedi",
      date: "2021-10-11",
      time: "22:00",
      language: "VO",
      reservation_link: "https://codephenix.fr",
    },
    {
      day: "Dimanche",
      date: "2021-10-12",
      time: "22:00",
      language: "VO",
      reservation_link: "https://codephenix.fr",
    },
  ],
};

const theater = {
  id: "1",
  name: "MK2 Bibliothèque",
  address: "2 rue de la bibliothèque, 75014 Paris",
  accessibility_description:
    "La salle est plutôt accessible mais les escaliers sont un peu raides. Si vous faites de l'escalade ca devrait aller mais sinon partez plutôt sur l'option home cinema",
  photos: [sampleImage, sampleImage, sampleImage],
  movies_rooms: [movie_room, movie_room, movie_room],
} as Theater;

const getTheaterKey = (): APIQueryKey => ["get_theater_details"];
// const fetchTheaters = async (): Promise<Theater[]> => theaters;
const fetchTheater = (): Theater => theater;
export const useGetTheater = (): UseQueryResult<Theater> => {
  return useQuery({ queryKey: getTheaterKey(), queryFn: fetchTheater });
};
