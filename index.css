window.onload = function() {
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAvyn_qt-jyaPGxyeI4blOJgV9Jj4K3yIw",
  authDomain: "cyberprime-6f2ea.firebaseapp.com",
  projectId: "cyberprime-6f2ea",
  storageBucket: "cyberprime-6f2ea.appspot.com",
  messagingSenderId: "553253419304",
  appId: "1:553253419304:web:3e46876032f2c80f15781d",
  measurementId: "G-9TW1R2G057"
};
 // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  var db = firebase.database();

  class MEME_CHAT {
    home() {
      document.body.innerHTML = '';
      this.create_title();
      this.create_join_form();
    }

    chat() {
      this.create_title();
      this.create_chat();
    }

    create_title() {
      var title_container = document.createElement('div');
      title_container.setAttribute('id', 'title_container');
      var title_inner_container = document.createElement('div');
      title_inner_container.setAttribute('id', 'title_inner_container');
      var title = document.createElement('h1');
      title.setAttribute('id', 'title');
      title.textContent = 'CYBERPRIME';
      title_inner_container.append(title);
      title_container.append(title_inner_container);
      document.body.append(title_container);

      // Logout Button
      var logout_button = document.createElement('button');
      logout_button.setAttribute('id', 'logout_button');
      logout_button.textContent = 'Logout';
      title_inner_container.append(logout_button);

      var parent = this;
      logout_button.onclick = function() {
        parent.logout();
      };
    }

    create_join_form() {
      var parent = this;
      var join_container = document.createElement('div');
      join_container.setAttribute('id', 'join_container');
      var join_inner_container = document.createElement('div');
      join_inner_container.setAttribute('id', 'join_inner_container');
      var join_button_container = document.createElement('div');
      join_button_container.setAttribute('id', 'join_button_container');
      var join_button = document.createElement('button');
      join_button.setAttribute('id', 'join_button');
      join_button.innerHTML = 'Join <i class="fas fa-sign-in-alt"></i>';
      var join_input_container = document.createElement('div');
      join_input_container.setAttribute('id', 'join_input_container');
      var join_input = document.createElement('input');
      join_input.setAttribute('id', 'join_input');
      join_input.setAttribute('maxlength', 15);
      join_input.placeholder = 'Enter your username';
      join_input.onkeyup = function(event) {
        if (join_input.value.length > 0) {
          join_button.classList.add('enabled');
          if (event.key === 'Enter') {
            parent.save_name(join_input.value);
            join_container.remove();
            parent.create_chat();
          }
        } else {
          join_button.classList.remove('enabled');
        }
      };

      join_button.onclick = function() {
        parent.save_name(join_input.value);
        join_container.remove();
        parent.create_chat();
      };

      join_button_container.append(join_button);
      join_input_container.append(join_input);
      join_inner_container.append(join_input_container, join_button_container);
      join_container.append(join_inner_container);
      document.body.append(join_container);
    }

    create_load(container_id) {
      var parent = this;
      var container = document.getElementById(container_id);
      container.innerHTML = '';
      var loader_container = document.createElement('div');
      loader_container.setAttribute('class', 'loader_container');
      var loader = document.createElement('div');
      loader.setAttribute('class', 'loader');
      loader_container.append(loader);
      container.append(loader_container);
      setTimeout(function() {
        parent.scroll_bottom(container_id);
      }, 200);
    }

    create_chat() {
      var parent = this;
      var chat_container = document.createElement('div');
      chat_container.setAttribute('id', 'chat_container');
      var chat_content_container = document.createElement('div');
      chat_content_container.setAttribute('id', 'chat_content_container');
      var chat_input_container = document.createElement('div');
      chat_input_container.setAttribute('id', 'chat_input_container');
      var chat_input_send = document.createElement('button');
      chat_input_send.setAttribute('id', 'chat_input_send');
      chat_input_send.innerHTML = '<i class="fas fa-paper-plane"></i>';
      var chat_input = document.createElement('input');
      chat_input.setAttribute('id', 'chat_input');
      chat_input.setAttribute('maxlength', 1000);
      chat_input.placeholder = 'Say something...';

      chat_input.addEventListener('keydown', function(event) {
        if (event.keyCode === 13) {
          event.preventDefault();
          if (chat_input.value.length > 0) {
            chat_input_send.setAttribute('disabled', true);
            chat_input_send.classList.remove('enabled');
            parent.create_load('chat_content_container');
            parent.send_message(chat_input.value);
            chat_input.value = '';
            chat_input.focus();
          }
        }
      });

      chat_input_send.onclick = function() {
        if (chat_input.value.length > 0) {
          chat_input_send.setAttribute('disabled', true);
          chat_input_send.classList.remove('enabled');
          parent.create_load('chat_content_container');
          parent.send_message(chat_input.value);
          chat_input.value = '';
          chat_input.focus();
        }
      };

      chat_input.onkeyup = function() {
        if (chat_input.value.length > 0) {
          chat_input_send.classList.add('enabled');
        } else {
          chat_input_send.classList.remove('enabled');
        }
      };

      chat_input_container.append(chat_input, chat_input_send);
      chat_container.append(chat_content_container, chat_input_container);
      document.body.append(chat_container);

      parent.get_messages();
    }

    scroll_bottom(container_id) {
      var container = document.getElementById(container_id);
      container.scrollTop = container.scrollHeight;
    }

    save_name(name) {
      localStorage.setItem('name', name);
    }

    get_name() {
      return localStorage.getItem('name');
    }

    send_message(message) {
      var timestamp = Date.now();
      var data = {
        name: this.get_name(),
        message: message,
        timestamp: timestamp
      };
      db.ref('messages/' + timestamp).set(data);
    }

    get_messages() {
      var parent = this;
      var messages_ref = db.ref('messages/').orderByChild('timestamp');
      messages_ref.on('value', function(snapshot) {
        var messages = snapshot.val();
        var chat_content_container = document.getElementById('chat_content_container');
        chat_content_container.innerHTML = '';
        if (messages) {
          Object.keys(messages).forEach(function(key) {
            var message = messages[key];
            parent.create_message(message.name, message.message, message.timestamp);
          });
        }
        parent.scroll_bottom('chat_content_container');
      });
    }

    create_message(name, message, timestamp) {
      var chat_content_container = document.getElementById('chat_content_container');
      var message_container = document.createElement('div');
      message_container.setAttribute('class', 'message_container');
      var name_element = document.createElement('p');
      name_element.setAttribute('class', 'name');
      name_element.textContent = name;
      var message_element = document.createElement('p');
      message_element.setAttribute('class', 'message');
      message_element.textContent = message;
      var timestamp_element = document.createElement('p');
      timestamp_element.setAttribute('class', 'timestamp');
      timestamp_element.textContent = new Date(timestamp).toLocaleTimeString();

      message_container.append(name_element, message_element, timestamp_element);
      chat_content_container.append(message_container);
    }

    logout() {
      localStorage.removeItem('name');
      location.reload();
    }

    kick_user(name) {
      var kickRef = db.ref('kickedUsers/');
      kickRef.push().set(name);
    }
  }

  var chat = new MEME_CHAT();
  chat.home();
};
