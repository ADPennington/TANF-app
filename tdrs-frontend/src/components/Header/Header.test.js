import React from 'react'
import thunk from 'redux-thunk'
import { mount } from 'enzyme'
import { Provider } from 'react-redux'
import configureStore from 'redux-mock-store'

import { render } from '@testing-library/react'
import Header from './Header'

describe('Header', () => {
  const initialState = {
    router: { location: { pathname: '/profile' } },
    auth: {
      user: {
        email: 'test@test.com',
        roles: [{ id: 1, name: 'OFA System Admin', permissions: [] }],
      },
      authenticated: true,
    },
  }
  const mockStore = configureStore([thunk])

  it('should have a title link', () => {
    const store = mockStore(initialState)
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )

    const title = wrapper.find('a[title="Home"]')
    expect(title).toExist()
    expect(title).toIncludeText('TANF Data Portal')
  })

  it('should have a navigation link for Welcome', () => {
    const store = mockStore(initialState)
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )
    const welcomeLink = wrapper.find('#welcome')
    expect(welcomeLink).toExist()
    expect(welcomeLink).toIncludeText('Welcome')
  })

  it('should have a navigation link for dataFiles', () => {
    const store = mockStore(initialState)
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )
    const dataFilesLink = wrapper.find('#data-files')
    expect(dataFilesLink).toExist()
    expect(dataFilesLink).toIncludeText('Data Files')
  })

  it('should have a navigation link for Profile', () => {
    const store = mockStore(initialState)
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )
    const profileLink = wrapper.find('#profile')
    expect(profileLink).toExist()
    expect(profileLink).toIncludeText('Profile')
  })

  it('should have a navigation link for Admin when user is a OFA System Admin', () => {
    const store = mockStore(initialState)
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )
    const adminLink = wrapper.find('#admin')
    expect(adminLink).toExist()
    expect(adminLink).toIncludeText('Admin')
  })

  it('should NOT have a navigation link for Admin when user is NOT a OFA System Admin', () => {
    const store = mockStore({
      ...initialState,
      auth: {
        authenticated: true,
        user: {
          email: 'test@test.com',
          roles: [{ id: 2, name: 'Data Prepper', permissions: [] }],
        },
      },
    })

    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )
    const adminLink = wrapper.find('#admin')
    expect(adminLink).not.toExist()
    expect(adminLink).not.toIncludeText('Admin')
  })

  it('should find menu button', () => {
    const store = mockStore(initialState)
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )
    const menuBtn = wrapper.find('.usa-menu-btn')
    expect(menuBtn).toExist()
  })

  it("should add usa-current class to Welcome tab when on '/home'", () => {
    const store = mockStore({
      ...initialState,
      router: { location: { pathname: '/home' } },
    })
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )

    const welcomeTab = wrapper.find('#welcome')

    expect(welcomeTab.hasClass('usa-current')).toEqual(true)
  })

  it("should add usa-current class to Data Files tab when on '/data-files'", () => {
    const store = mockStore({
      ...initialState,
      router: { location: { pathname: '/data-files' } },
    })
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )

    const dataFilesTab = wrapper.find('#data-files')

    expect(dataFilesTab.hasClass('usa-current')).toEqual(true)
  })

  it("should add usa-current class to Profile tab when on '/profile'", () => {
    const store = mockStore(initialState)
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )

    const profileTab = wrapper.find('#profile')

    expect(profileTab.hasClass('usa-current')).toEqual(true)
  })

  it("should not add usa-current class to Welcome tab when not on '/'", () => {
    const state = { ...initialState, router: { location: { pathname: '/' } } }
    const store = mockStore(state)
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )

    const welcomeTab = wrapper.find('#welcome')

    expect(welcomeTab.hasClass('usa-current')).toEqual(false)
  })

  it('should have secondaryItems when user is logged in', () => {
    const store = mockStore(initialState)
    const wrapper = mount(
      <Provider store={store}>
        <Header />
      </Provider>
    )

    const secondaryLinks = wrapper.find('.usa-nav__secondary-item')

    expect(secondaryLinks.length).toEqual(2)
    expect(secondaryLinks.first().text()).toEqual('test@test.com')
  })

  it('should NOT show any nav items when the user is NOT logged in', () => {
    const state = {
      ...initialState,
      auth: { user: {}, authenticated: false },
    }

    const store = mockStore(state)

    const { queryByText } = render(
      <Provider store={store}>
        <Header />
      </Provider>
    )

    expect(queryByText('Welcome')).not.toBeInTheDocument()
    expect(queryByText('Data Files')).not.toBeInTheDocument()
    expect(queryByText('Profile')).not.toBeInTheDocument()
    expect(queryByText('Admin')).not.toBeInTheDocument()
  })
})
