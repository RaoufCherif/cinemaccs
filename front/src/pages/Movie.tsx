import { useGetMovie } from "../data/movie";
import { Flex, Box, Stack, Image, Link, Spinner } from "@chakra-ui/react";

import { MovieWithTheaters, Room, Session, Theater } from "./types";
import { useEffect, useState } from "react";
import { ExternalLinkIcon } from "@chakra-ui/icons";

type SessionEnriched = Session & {
  theater_id: number;
  theater_name: string;
  theater_logo?: string;
  room_id: number;
  room_name: string;
  room_accessibility_description: string;
};

const MovieCard: React.FC<{ movie: MovieWithTheaters }> = ({ movie }) => {
  return (
    <Box>
      <Flex>
        <Image src={`data:image/jpeg;base64, ${movie.poster}`} />
        <Flex ml={2} flexDir="column">
          <Box>{movie.title}</Box>
          <Box>{movie.duration}</Box>
          <Link href={`${movie.allocine_link}`} isExternal>
            Lien vers allocine
            <ExternalLinkIcon mx={1} />
          </Link>
        </Flex>
      </Flex>
    </Box>
  );
};
export const MoviePage = () => {
  const { isLoading, data: movie } = useGetMovie();
  const [sessions, setSessions] = useState<SessionEnriched[]>([]);
  useEffect(() => {
    const result = [] as SessionEnriched[];
    if (movie) {
      for (const theater of movie?.theaters) {
        for (const room of theater.rooms) {
          for (const session of room.sessions) {
            result.push({
              ...session,
              theater_id: theater.id,
              theater_name: theater.name,
              // theater_logo: theater.,
              room_id: room.id,
              room_name: room.name,
              room_accessibility_description: room.accessibility_description,
            });
          }
        }
      }
      setSessions(result);
    }
  }, [movie]);
  if (isLoading) {
    return <Spinner />;
  }
  return (
    <Flex
      flexDirection="column"
      width="100wh"
      height="100vh"
      backgroundColor="gray.200"
      justifyContent="center"
      alignItems="center"
    >
      <Stack
        flexDir="column"
        mb="2"
        justifyContent="center"
        alignItems="center"
      >
        {movie ? (
          <>
            <MovieCard movie={movie} />
            <Box minW={{ base: "90%", md: "468px" }}>
              <Stack
                spacing={4}
                p="1rem"
                backgroundColor="whiteAlpha.900"
                boxShadow="md"
              >
                {sessions ? (
                  sessions.map((session, idx) => (
                    <Link href={`/rooms/${session.room_id}`} key={idx}>
                      {session.theater_name} - {session.room_name}
                    </Link>
                  ))
                ) : (
                  <div>Aucun résultat</div>
                )}
              </Stack>
            </Box>
          </>
        ) : (
          <Box>Film introuvable</Box>
        )}
      </Stack>
    </Flex>
  );
};
