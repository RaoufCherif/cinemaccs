import { useGetMovie } from "../data/movie";
import {
  Card,
  Text,
  Box,
  Stack,
  Image,
  Link,
  Spinner,
  CardBody,
  CardFooter,
  Button,
  Heading,
} from "@chakra-ui/react";

import { MovieWithTheaters, Session } from "./types";
import { useEffect, useState } from "react";
import { ExternalLinkIcon } from "@chakra-ui/icons";
import { PageLayout } from "../components/PageLayout";

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
    <Card
      direction={{ base: "column", sm: "row" }}
      overflow="hidden"
      variant="outline"
    >
      <Image
        objectFit="cover"
        maxW={{ base: "100%", sm: "200px" }}
        src={`data:image/jpeg;base64, ${movie.poster}`}
        alt="Caffe Latte"
      />

      <Stack>
        <CardBody>
          <Heading size="md">{movie.title}</Heading>
          <Text py="2">{movie.duration}</Text>
          <Link href={`${movie.allocine_link}`} isExternal>
            Lien vers allocine
            <ExternalLinkIcon mx={1} />
          </Link>
        </CardBody>

        <CardFooter>
          <Button variant="solid" colorScheme="blue">
            Buy Latte
          </Button>
        </CardFooter>
      </Stack>
    </Card>
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
  return (
    <PageLayout isLoading={isLoading}>
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
    </PageLayout>
  );
};
