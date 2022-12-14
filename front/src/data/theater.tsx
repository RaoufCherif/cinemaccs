import { useQuery, UseQueryResult } from "@tanstack/react-query";
import { Theater } from "../pages/types";
import { APIQueryKey } from "./utils";

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
