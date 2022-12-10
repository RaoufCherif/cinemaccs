# For production, use node as build container only
# https://collabnix.com/creating-your-first-react-app-using-docker/

# FROM node:19.1 AS development
FROM node:19.1

# ENV NODE_ENV development
# Add a work directory
WORKDIR /app

# Cache and Install dependencies
COPY package.json .
COPY yarn.lock .
RUN yarn install
# Copy app files
COPY . ./
# Expose port
EXPOSE 3000
# Start the app
CMD [ "yarn", "start" ]