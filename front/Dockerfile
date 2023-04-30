# Use an official Node.js runtime as a parent image
FROM node:current-bullseye-slim

# Set the working directory to /app
WORKDIR /app

# Copy the package.json and package-lock.json files into the container at /app
COPY front/package*.json ./

# Install any needed packages specified in package.json
RUN npm install

# Copy the rest of the application code into the container at /app
COPY . .

# Build the React app
RUN pnpm run build

# Expose port 3000 for the React app to listen on
EXPOSE 3000

# Start the React app when the container is started
CMD [ "npm", "run", "dev" ]