# Build stage
FROM node:25-alpine AS builder

WORKDIR /frontend

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm run build

# Production stage
FROM node:25-alpine

WORKDIR /frontend

RUN npm install -g serve

COPY --from=builder /frontend/dist ./dist

EXPOSE 3000

CMD ["serve", "-s", "dist", "-l", "3000"]