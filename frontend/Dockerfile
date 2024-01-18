# Use an official Nginx image as a parent image
FROM nginx:alpine

# Copy the HTML, CSS, and JavaScript files to the Nginx server
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]

