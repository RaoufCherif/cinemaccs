import * as React from "react";
import { useEffect, useState } from "react";
import {
  Card,
  CardBody,
  CardFooter,
  Button,
  Heading,
  Text,
  Flex,
  Box,
  Stack,
  Image,
} from "@chakra-ui/react";
import { MovieRoom, Day, TheaterBase } from "../pages/types";
import { sampleImage } from "../sample_image";

export const TheaterCard: React.FC<{ theater: TheaterBase }> = ({
  theater,
}) => {
  const [imageSrc, setImgSrc] = useState("");
  useEffect(() => {
    setImgSrc(theater.photos?.length ? theater.photos[0] : sampleImage);
  }, [theater]);
  return (
    <Box>
      <Flex>
        <Image src={`data:image/jpeg;base64, ${imageSrc}`} />
        <Flex ml={2} flexDir="column">
          <Box>{theater.name}</Box>
          <Box>{theater.address}</Box>
          <Box>{theater.accessibility_description}</Box>
        </Flex>
      </Flex>
      {!!theater.photos?.length && (
        <Flex mt={2}>
          {theater.photos.map((photo, idx) => (
            <Image
              width="100px"
              mr={3}
              key={`photo-${idx}`}
              src={`data:image/jpeg;base64, ${photo}`}
            />
          ))}
        </Flex>
      )}
    </Box>
  );
};

export const MovieRoomCard: React.FC<{ movieRoom: MovieRoom; day: Day }> = ({
  movieRoom,
  day,
}) => {
  const { movie, room, sessions } = movieRoom;

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
          <Heading size="md">
            {movie.title} - {room.name}
          </Heading>
          {sessions.map(
            (session, idx) =>
              session.day === day && (
                <Box key={`session-${idx}`} backgroundColor="yellow.300" mr={2}>
                  <Text>{session.language}</Text>
                  <Text>{session.time}</Text>
                </Box>
              ),
          )}
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
