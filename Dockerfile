### Dockerfile for Mollufier ###

## FRONTEND BUILDER ##
# Use Debian Bullseye based Node.js 16 LTS image
FROM node:16-bullseye-slim AS builder

# Buid arguments
ARG FE_PUBLIC_PATH="/"
ENV PUBLIC_PATH=${FE_PUBLIC_PATH}

ARG FE_BACKEND_BASE_URL="/api"
ENV BACKEND_BASE_URL=${FE_BACKEND_BASE_URL}

ARG FE_GA_MEASUREMENT_ID=""
ENV GA_MEASUREMENT_ID=${FE_GA_MEASUREMENT_ID}

# Install Node.js global dependencies
RUN npm install -f --location=global yarn @vue/cli

# Working directory
WORKDIR /build

# Copy frontend sources and create .env.local
COPY frontend .
RUN echo "" > .env.local; \
    echo "VUE_APP_BACKEND_BASE_URL=\"${BACKEND_BASE_URL}\"" >> .env.local; \
    echo "VUE_APP_GA_MEASUREMENT_ID=\"${GA_MEASUREMENT_ID}\"" >> .env.local

# Do build
RUN yarn install
RUN rm -rf ./dist && yarn build --mode production


## SERVICE CONTAINER ##
# Use Debian Bullseye based Node.js 16 LTS image
# We can't use Alpine based image due to error with Kiwi dependency installation
FROM node:16-bullseye-slim AS runner

# Container labels
LABEL org.opencontainers.image.title="Mollufier"
LABEL org.opencontainers.image.description="Mollufies sentences using Korean tokenizer"
LABEL org.opencontainers.image.authors="somni <me@somni.one>"
LABEL org.opencontainers.image.url="https://github.com/somnisomni/mollufier"
LABEL org.opencontainers.image.documentation="https://github.com/somnisomni/mollufier"
LABEL org.opencontainers.image.source="https://github.com/somnisomni/mollufier"
LABEL org.opencontainers.image.licenses="MIT"

# Install Python 3
RUN apt-get -y update \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js global dependencies
RUN npm install -f --location=global http-server

# Working directory
WORKDIR /app

# Copy service files to app directory
RUN mkdir -p backend && mkdir -p frontend
COPY backend backend
COPY --from=builder /build/dist frontend

# Install backend dependencies
RUN pip3 install -r ./backend/requirements.txt

# Entrypoint / CMD
COPY container-entrypoint.sh .
ENTRYPOINT ["/bin/bash", "container-entrypoint.sh"]

# Exposes
EXPOSE 8080 8081
