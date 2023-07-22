import { Flex, Box, Text, Stack, Spinner, Image } from "@chakra-ui/react";

import { useGetRoom } from "../data/room";
import { PageLayout } from "../components/PageLayout";
import { TheaterCard } from "../components/Cards";

export const RoomPage = () => {
  const { isLoading, data: room } = useGetRoom();
  if (isLoading) {
    return <Spinner />;
  }
  return (
    <PageLayout>
      {room ? (
        <>
          <TheaterCard theater={room.theater} />
          <Flex flexDirection={"column"}>
            <Text>
              Description générale du cinéma:{" "}
              {room.theater.accessibility_description}
            </Text>
            <Text>Entrée du cinéma: {room.theater.entry_description}</Text>
            <Text>
              Toilettes du cinéma: {room.theater.sanitory_description}
            </Text>
            <Text>Boutique du cinéma: {room.theater.popcorn_description}</Text>
            <Text>
              Description de la salle: {room.accessibility_description}
            </Text>
            <Text>Entrée de la salle: {room.access_point}</Text>
          </Flex>
          {room.photos && (
            <Stack>
              Photos du cinéma:{" "}
              {room.photos.map((photo) => (
                <Image src={`data:image/jpeg;base64, ${photo}`} />
              ))}
            </Stack>
          )}
        </>
      ) : (
        <Box>Salle introuvable</Box>
      )}
    </PageLayout>
  );
};
